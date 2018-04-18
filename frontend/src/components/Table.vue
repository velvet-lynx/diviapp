<template>
  <table v-if="datas" class="ui celled table">
    <TableHeader :titles="titles" />
    <TableFooter :titles="titles" />
    <tbody>
      <TableRow v-for="(row, index) in datas" :key="index" :datas="row" />
    </tbody>
  </table>
</template>

<script>
import TableRow from "./TableRow.vue"
import TableHeader from "./TableHeader.vue"
import TableFooter from "./TableFooter.vue"

export default {
  name: "Table",
  props: ['datas'],
  computed: {
    columns(){
      return Object.keys(this.datas[0]);
    }
  },
  components:{
    TableRow,
    TableHeader,
    TableFooter
  },
  computed: {
    titles() {
      return Object.keys(this.datas[0]);
    }
  }

}
</script>
