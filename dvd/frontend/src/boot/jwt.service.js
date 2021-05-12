
export const getToken = () => {
  console.log("mirame")
  return window.localStorage.getItem('authToken')
}

export const saveToken = (token) => {
  console.log("mirame 2")
  window.localStorage.setItem('authToken', token)
}

export const destroyToken = () => {
  window.localStorage.removeItem('authToken')
}

export default { getToken, saveToken, destroyToken }
