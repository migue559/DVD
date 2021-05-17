
export const getToken = () => {
  return window.localStorage.getItem('authToken')
}

export const saveToken = (token) => {
  window.localStorage.setItem('authToken', token)
}

export const destroyToken = () => {
  window.localStorage.removeItem('authToken')
}

export default { getToken, saveToken, destroyToken }
