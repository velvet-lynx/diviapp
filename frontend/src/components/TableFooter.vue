<template>
  <tfoot>
    <th v-for="title in titles" :key="title">{{ title }}</th>
  </tfoot>
</template>

<script>
export default {
  name: 'TableFooter',
  props: ['titles'],
}
</script>
