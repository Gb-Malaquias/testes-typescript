// Funções matemáticas simples para testar
export function soma(a: number, b: number): number {
    return a + b
  }
  
  export function media(valores: number[]): number {
    if (valores.length === 0) return 0
    const soma = valores.reduce((acc, val) => acc + val, 0)
    return soma / valores.length
  }
  