export const getDate = (): string => {
  const dateObj = new Date()
  const day = dateObj.getDate()
  const month = dateObj.getMonth()
  const year = dateObj.getFullYear()
  
  return `${day < 10 ? '0'.concat(String(day)): day}${month < 10 ? '0'.concat(String(month)): month}${year}`
}