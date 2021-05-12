
import JwtService from '@boot/jwt.service'
import { apollo } from '@boot/apollo'
import { tokenAuth, verifyToken } from '@endpoints/auth.endpoints'

const state = {
  user: [],
  isAuthenticated: !!JwtService.getToken(),
  authenting: false,
  errors: []
}

const getters = {
}

const actions = {
  login (context, credentials) {
    context.commit('setAuthenting')
    return apollo
      .mutate({
        mutation: tokenAuth(credentials)
      }).then(({ data }) => {
        context.commit('setAuth', data.tokenAuth)
        return data.tokenAuth
      }).catch((error) => {
        console.error(error)
        context.commit('setErrors', error)
      })
  },
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
}

const mutations = {
  setAuthenting (state) {
    state.authenting = true
  },
  setAuth (state, tokenAuth) {
    state.user = tokenAuth.payload
    if ('token' in tokenAuth) JwtService.saveToken(tokenAuth.token)
    state.authenting = false
    state.isAuthenticated = true
  },
  setErrors (state, error) {
    state.errors = [error]
    state.authenting = false
  },
  purgeAuth (state) {
    JwtService.destroyToken()
    state.isAuthenticated = false
    state.authenting = false
    state.user = []
    state.errors = []
  }
}

export default {
  state,
  actions,
  mutations,
  getters
}
