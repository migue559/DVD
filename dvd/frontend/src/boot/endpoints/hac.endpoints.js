import gql from 'graphql-tag'

export const cataloguesHiveQuery = (key) => {
  const nameIcontains = key ? `name_Icontains:"${key}"` : ''
  return gql`
  query{
    hiveCatalogueQuery(
      first:100
      ${nameIcontains}
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
