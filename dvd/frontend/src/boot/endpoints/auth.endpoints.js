import gql from 'graphql-tag'

export const tokenAuth = (credentials) => {

  return gql`
    mutation {
      tokenAuth (
        username:"${credentials.username}"
        password:"${credentials.password}"
      )
      {
        token
        payload
      }
    }
  `
}

export const verifyToken = (token) => {
  return gql`
    mutation{
      verifyToken(token: "${token}"){
        payload
      }
    }
  `
}
