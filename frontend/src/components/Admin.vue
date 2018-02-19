<template>
  <div class="ui raised container segment">
    <Table :datas="lines" />
  </div>
</template>

<script>
import axios from 'axios'
import Table from "./Table.vue"

export default {
  name: 'admin',
  data() {
    return {
      baseUrl: "http://localhost:5000",
      lines: []
    }
  },
  components: {
    Table
  },
  mounted() {
    axios.get(this.baseUrl+'/lines/').then(response => this.lines = response.data);
  }
}
</script>

<style>

</style>
