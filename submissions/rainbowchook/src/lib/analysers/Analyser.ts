export interface Analyser<T> {
  run(arr: T[]): string
}
