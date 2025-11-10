import { describe, it, expect } from "vitest"
import { soma, media } from "./math"

describe("Testes do módulo math", () => {
  it("deve somar dois números corretamente", () => {
    expect(soma(2, 3)).toBe(5)
  })

  it("deve retornar a média correta de um array de números", () => {
    const resultado = media([4, 6, 8])
    expect(resultado).toBeCloseTo(6)
  })

  it("deve retornar 0 para um array vazio", () => {
    expect(media([])).toBe(0)
  })
})
