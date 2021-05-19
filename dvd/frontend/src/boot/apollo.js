import { boot } from 'quasar/wrappers'
import { ApolloClient, createHttpLink, InMemoryCache, split } from '@apollo/client/core'
import { WebSocketLink } from '@apollo/client/link/ws'
import { getMainDefinition } from '@apollo/client/utilities'
import { setContext } from 'apollo-link-context'
import JwtService from '@boot/jwt.service'


const GRAPHQL_URL = process.env.APOLLOHTTP
const GRAPHQLWS_URL = process.env.APOLLOWS

const getHeaders = () => {
  const headers = {
    authorization: ''
  }
  headers.authorization = JwtService.getToken() ? `JWT ${JwtService.getToken()}` : ''
  //headers.authorization = `JWT ${JwtService.getToken()}`
  return headers
}

const headerLink = setContext(() => {
  return {
    headers: {
      //authorization: `JWT ${JwtService.getToken()}`
      authorization: JwtService.getToken() ? `JWT ${JwtService.getToken()}` : ''
    }
  }
})

const httpLink = createHttpLink({
  uri: GRAPHQL_URL,
  fetch,
  headers: getHeaders(),

})

const wsLink = new WebSocketLink({
  uri: GRAPHQLWS_URL,
  headers: getHeaders(),
  options: {
    reconnect: true
  }
})

const link = split(
  ({ query }) => {
    const definition = getMainDefinition(query)
    return definition.kind === 'OperationDefinition' &&
      definition.operation === 'subscription'
  },
  wsLink,
  httpLink
)

const apolloClient = new ApolloClient({
  link: headerLink.concat(link),
  cache: new InMemoryCache(),
  connectToDevTools: true,

})

const apollo = apolloClient

export default boot(({ app }) => {
  app.config.globalProperties.$apollo = apollo
})

export { apollo }
