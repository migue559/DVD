import JwtService from '@boot/jwt.service'
import { apollo } from '@boot/apollo'
import { tokenAuth, verifyToken } from '@endpoints/auth.endpoints'


const state = {
  user: [],
  //isAuthenticated: !!JwtService.getToken(),
  authenting: false,
  errors: []
}

const getters = {
}

const actions = {
  login (context, userCredential) {
    console.log(">>>")
    console.log(userCredential)
    context.commit('setAuthenting')
    return apollo
      .mutate({
        mutation: tokenAuth(userCredential)
      }).then(({ data }) => {
        context.commit('setAuth', data.tokenAuth)
        return data.tokenAuth
      }).catch((error) => {
        console.error(error)
        context.commit('setErrors', error)
      })
  },
  /*
  logout (context) {
    context.commit('purgeAuth')
  },
  verifyAuth (context) {
    const token = JwtService.getToken()
    if (!token) return 0
    apollo
      .mutate({
        mutation: verifyToken(token)
      }).then(({ data }) => {
        context.commit('setAuth', data.verifyToken)
      })
      .catch(() => {
        context.commit('purgeAuth')
      })
  }
  */
}



export default {
  state,
  actions,
  //mutations,
  getters
}
