<template lang="pug">
q-page
    | columns {{ dataHive.columns}}
    | data {{ dataHive.rows[0]}}
    .q-pa-md
      q-table(title='Treats', dense='', :rows='dataHive.rows',  row-key='index_data')
    .q-pa-md
      q-table(:rows='dataHive.rows', title='QDataTable with QPopupEdit', :rows-per-page-options='[]', row-key='index_data')
        template(v-slot:body='props')
          q-tr(:props='props')
            q-td(key='desc', :props='props')
              | {{ props.row.index_data }}
              q-popup-edit(v-model='props.row.index_data', title='Edit the Name', auto-save='', v-slot='scope')
                q-input(v-model='scope.value', dense='', autofocus='', counter='', @keyup.enter='scope.set')
            q-td(key='calories', :props='props')
              | {{ props.row.calories }}
              q-popup-edit(v-model.number='props.row.calories', auto-save='', v-slot='scope')
                q-input(type='number', v-model.number='scope.value', dense='', autofocus='', @keyup.enter='scope.set')
            q-td(key='fat', :props='props')
              | {{ props.row.fat }}
              q-popup-edit(disable='', v-model='props.row.fat', auto-save='', v-slot='scope')
                .text-italic.text-primary.q-mb-xs
                  | My Custom Title
                q-input(v-model='scope.value', dense='', autofocus='', @keyup.enter='scope.set')
            q-td(key='carbs', :props='props')
              | {{ props.row.carbs }}
            q-td(key='protein', :props='props')
              | {{ props.row.protein }}
            q-td(key='sodium', :props='props')
              | {{ props.row.sodium }}
            q-td(key='calcium', :props='props')
              | {{ props.row.calcium }}
            q-td(key='iron', :props='props')
              | {{ props.row.iron }}



</template>

<script>
import { defineComponent, toRef,reactive, ref} from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { getHiveGetDataIDQuery, getHiveSchemaIDQuery } from '@endpoints/hac.endpoints'
import { apollo } from '@boot/apollo';

function getDataTable (id) {
  const route = useRoute()
  console.log(`este es mi parametro id : ${route.params.id}`)
  const dataHive = reactive({
    data: {},
    columns:{},
    rows:[]
  })
  const recoverColumns = () => {
    apollo
      .query({
        query: getHiveSchemaIDQuery(route.params.id)
      }).then(({ data }) => {
        dataHive.columns = JSON.parse(data.hiveSchemaID).map( (item) =>{
          return {
            name:item[0].split('.')[1]
          }
        })
      }).catch((error) => {
        console.error('hiveSchemaID error, recoverData:', error)
      })
  }
  const recoverData = () => {
    apollo
      .query({
        query: getHiveGetDataIDQuery(route.params.id)
      }).then(({ data }) => {
        dataHive.rows = eval(JSON.parse(data.hiveGetDataID)).map( (row) =>{
          const res = {}
          row.map( (col, idx) =>{
            res[dataHive.columns[idx].name] = col
            return col
          })
          return res
        })
      }).catch((error) => {
        console.error('hiveSchemaID error, recoverData:', error)
      })
  }
  recoverColumns()
  recoverData()


  return { dataHive }
}
const columns = [
  { name: 'desc', align: 'left', label: 'Dessert (100g serving)', field: 'name' },
  { name: 'calories', align: 'center', label: 'Calories', field: 'calories' },
  { name: 'fat', label: 'Fat (g)', field: 'fat' },
  { name: 'carbs', label: 'Carbs (g)', field: 'carbs' },
  { name: 'protein', label: 'Protein (g)', field: 'protein' },
  { name: 'sodium', label: 'Sodium (mg)', field: 'sodium' },
  { name: 'calcium', label: 'Calcium (%)', field: 'calcium' },
  { name: 'iron', label: 'Iron (%)', field: 'iron' }
]

const rows = [
  {
    name: 'Frozen Yogurt',
    calories: 159,
    fat: 6.0,
    carbs: 24,
    protein: 4.0,
    sodium: 87,
    calcium: '14%',
    iron: '1%'
  },
  {
    name: 'Ice cream sandwich',
    calories: 237,
    fat: 9.0,
    carbs: 37,
    protein: 4.3,
    sodium: 129,
    calcium: '8%',
    iron: '1%'
  },]


export default defineComponent({
  name: 'PageTable',

  setup() {

    return {
      ...getDataTable(),
      columns,
      rows:ref(rows),


    }

  }
})
</script>
