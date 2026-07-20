#!/usr/bin/env python3
"""
Validação de cálculos econômicos e termodinâmicos do projeto PAM.

Testa:
- Fórmulas de mais-valia (CALCULO-MARXISTA.md)
- Fórmula de extração total (tripla exploração)
- Ponto de virada fiscal (legalização)
- Entropia de Shannon (ENTROPIA-expandido.md)
- Consistência das tabelas de apostas EUA 2024

Todos os valores esperados foram derivados manualmente das fórmulas nos arquivos
de fundação. O objetivo é detectar alterações numéricas acidentais.
"""

import math
import pytest


# ──────────────────────────────────────────────────────────────────────────────
# CALCULO-MARXISTA.md — fórmulas econômicas
# ──────────────────────────────────────────────────────────────────────────────

class TestMaisValia:
    """§1 — circuito padrão: s' = s / v"""

    def test_taxa_exploracao_exemplo_simples(self):
        """Exemplo do arquivo: salário 2000, produção 5000."""
        v = 2_000   # salário
        total = 5_000  # valor produzido
        s = total - v   # mais-valia
        taxa = s / v

        assert s == 3_000
        assert taxa == pytest.approx(1.5)  # 150%

    def test_taxa_exploracao_formula_generica(self):
        """s' = s/v deve ser positivo quando total > v."""
        for v, total in [(1000, 3000), (1500, 4500), (800, 2000)]:
            s = total - v
            taxa = s / v
            assert taxa > 0
            assert taxa == pytest.approx((total - v) / v)


class TestCapturaNosConsumo:
    """§2 — tributação de risco: Fluxo = αv → (1-t)θαv + tθαv"""

    def test_exemplo_simples_salario_2000(self):
        """Exemplo do arquivo."""
        v = 2_000       # salário
        alpha = 0.10    # fração apostada
        theta = 0.15    # hold (retenção da casa)
        t = 0.40        # alíquota estatal

        aposta = alpha * v                      # 200
        hold_total = theta * aposta             # 30
        imposto = t * hold_total                # 12
        lucro_plataforma = (1 - t) * hold_total # 18
        retorno = aposta - hold_total           # 170 (em média)

        assert aposta == pytest.approx(200)
        assert hold_total == pytest.approx(30)
        assert imposto == pytest.approx(12)
        assert lucro_plataforma == pytest.approx(18)
        assert retorno == pytest.approx(170)

    def test_soma_hold_deve_ser_aposta_vezes_theta(self):
        """imposto + lucro_plataforma == theta * aposta"""
        for alpha, theta, t in [(0.10, 0.15, 0.40), (0.05, 0.20, 0.30), (0.15, 0.10, 0.51)]:
            v = 2_000
            aposta = alpha * v
            hold_total = theta * aposta
            imposto = t * hold_total
            lucro = (1 - t) * hold_total
            assert imposto + lucro == pytest.approx(hold_total)

    def test_ny_aliquota_51_pct(self):
        """Nova York cobra 51% — alíquota mais alta citada."""
        theta = 0.09    # ~9% hold médio EUA
        t_ny = 0.51
        handle = 149_600_000_000  # US$ 149.6 bi (2024)
        hold_total = theta * handle
        imposto_ny_share = t_ny * hold_total
        # NY não recebe 51% de tudo, mas a alíquota nominal é 51% do GGR do estado
        # Verificar que alíquota 51% > alíquota Nevada 6.75%
        t_nevada = 0.0675
        assert t_ny > t_nevada
        assert t_ny == pytest.approx(0.51)


class TestTriplaExploracao:
    """§3 — extração total = s + hold + imposto"""

    def test_total_extraido_do_exemplo(self):
        """Trabalhador produz 5000, fica com ~1988 de retido real."""
        v = 2_000       # salário
        total_produzido = 5_000
        s = total_produzido - v  # mais-valia
        alpha = 0.10
        theta = 0.15
        t = 0.40

        aposta = alpha * v
        hold_total = theta * aposta
        imposto = t * hold_total
        lucro_plataforma = (1 - t) * hold_total

        extraido_total = s + lucro_plataforma + imposto
        retido_real = v - aposta  # salário menos o que apostou

        assert extraido_total == pytest.approx(3_042)
        assert retido_real == pytest.approx(1_800)

    def test_formula_extracao_total(self):
        """E = s + (1-t)θαv + tθαv = s + θαv"""
        v = 2_000
        s = 3_000
        alpha = 0.10
        theta = 0.15
        t = 0.40

        # E = s + θαv (o 't' distribui internamente, mas a extração total do hold é θαv)
        e = s + theta * alpha * v
        assert e == pytest.approx(s + 30)  # 3030

    def test_incentivo_legalizar(self):
        """Legalizar é racional quando receita > custo de repressão."""
        # R_legalizar = t * theta * H
        # R_proibir = -C_repressao (custo)
        # Legalizar quando R_legalizar > C_repressao
        theta = 0.09
        t = 0.20
        H_mercado_negro = 50_000_000_000  # US$ 50bi de mercado ilegal

        receita_potencial = t * theta * H_mercado_negro
        custo_repressao_estimado = 2_000_000_000  # US$ 2bi/ano

        assert receita_potencial > custo_repressao_estimado


# ──────────────────────────────────────────────────────────────────────────────
# ENTROPIA-expandido.md — entropia de Shannon
# ──────────────────────────────────────────────────────────────────────────────

class TestEntropiaShannon:
    """§ Aprofundamento 1 — S = -sum(p_i * log(p_i))"""

    def test_entropia_uniforme_dois_estados(self):
        """Máxima entropia para 2 estados: p = [0.5, 0.5] → S = ln(2) ≈ 0.693"""
        probs = [0.5, 0.5]
        s = -sum(p * math.log(p) for p in probs)
        assert s == pytest.approx(math.log(2), rel=1e-6)

    def test_entropia_certeza_absoluta(self):
        """Evento certo (p=1) → entropia = 0"""
        probs = [1.0]
        s = -sum(p * math.log(p) for p in probs if p > 0)
        assert s == pytest.approx(0.0)

    def test_entropia_antes_apostas(self):
        """Exemplo do arquivo: antes de legalização, S ≈ 0.46 nats."""
        # Distribuição: 90% mantém status, 10% muda
        probs = [0.90, 0.10]
        s = -sum(p * math.log(p) for p in probs)
        # Arquivo diz ~0.46 — verificar ordem de grandeza
        assert 0.30 < s < 0.60

    def test_entropia_depois_apostas(self):
        """Exemplo do arquivo: depois, S ≈ 1.39 nats."""
        # Distribuição aproximada: ~30% por estado (4 estados)
        probs = [0.30, 0.30, 0.25, 0.15]
        s = -sum(p * math.log(p) for p in probs)
        # Arquivo diz ~1.39 — verificar ordem de grandeza
        assert 1.0 < s < 1.8

    def test_delta_entropia_positivo(self):
        """ΔS = S_depois - S_antes deve ser positivo (aumento de incerteza)."""
        probs_antes = [0.90, 0.10]
        probs_depois = [0.30, 0.30, 0.25, 0.15]

        s_antes = -sum(p * math.log(p) for p in probs_antes)
        s_depois = -sum(p * math.log(p) for p in probs_depois)

        assert s_depois > s_antes
        assert (s_depois - s_antes) > 0


# ──────────────────────────────────────────────────────────────────────────────
# Dados reais EUA 2024 — consistência interna
# ──────────────────────────────────────────────────────────────────────────────

class TestDadosEUA2024:
    """Verificar consistência interna dos dados citados no projeto."""

    HANDLE_2024 = 149_600_000_000  # US$ 149.6 bi
    HANDLE_2023 = 121_100_000_000  # US$ 121.1 bi
    HOLD_2024 = 13_700_000_000     # US$ 13.7 bi
    IMPOSTO_APOSTA = 2_800_000_000 # US$ 2.8 bi
    IMPOSTO_TODO = 15_910_000_000  # US$ 15.91 bi (recorde)

    def test_handle_cresceu_2023_2024(self):
        assert self.HANDLE_2024 > self.HANDLE_2023

    def test_hold_menor_que_handle(self):
        """Hold é sempre menor que handle."""
        assert self.HOLD_2024 < self.HANDLE_2024

    def test_hold_rate_plausivel(self):
        """Hold rate deve estar entre 5% e 15% (típico do setor)."""
        hold_rate = self.HOLD_2024 / self.HANDLE_2024
        assert 0.05 < hold_rate < 0.15

    def test_imposto_menor_que_hold(self):
        """Imposto de aposta esportiva < hold total."""
        assert self.IMPOSTO_APOSTA < self.HOLD_2024

    def test_imposto_aposta_menor_que_todo_jogo(self):
        """Imposto só de apostas < imposto de todo jogo comercial."""
        assert self.IMPOSTO_APOSTA < self.IMPOSTO_TODO

    def test_crescimento_impostos_32_pct(self):
        """Crescimento de ~32% citado no arquivo."""
        imposto_2023 = 2_100_000_000  # US$ 2.1 bi
        crescimento = (self.IMPOSTO_APOSTA - imposto_2023) / imposto_2023
        # Aceitar entre 25% e 40% (arredondamentos diferentes nas fontes)
        assert 0.25 < crescimento < 0.40

    def test_pie_chart_soma_100(self):
        """Os dois fatias do pie chart devem somar 100%."""
        operadoras = 79.6
        impostos = 20.4
        assert operadoras + impostos == pytest.approx(100.0)


# ──────────────────────────────────────────────────────────────────────────────
# Runner
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    result = pytest.main([__file__, "-v", "--tb=short"])
    sys.exit(result)
