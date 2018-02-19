<template>
  <thead>
    <tr>
      <th v-for="title in titles" :key="title">{{ title }}</th>
    </tr>
  </thead>
</template>

<script>
export default {
  name: 'TableHeader',
  props: ['titles'],
}
</script>
