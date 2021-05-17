import gql from 'graphql-tag'

//export const cataloguesHiveQuery = (key) => {
export const cataloguesHiveQuery = () => {
  return gql`
  query{
    hiveCatalogueQuery(
      first:100
    ) {
      edges {
        node {
          id
          name
          description
          catalogue
          views
          downloads
          isPublic

        }
      }
    }
  }
  `
}

export const singleHiveTableQuery = (id) => {
  console.log(`este es un id: ${id}`)
  return gql`
  query{
    hiveCatalogueID( id:"${id}")
    {id
      name
      description
      views
      downloads
      isPublic

    }
  }
  `
}
