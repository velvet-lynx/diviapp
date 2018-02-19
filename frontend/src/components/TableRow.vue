<template>
  <tr>
    <td v-for="(value, key) in datas" :key="key">
      <div class="ui input fluid">
        <input type="text" class="input" :value="value">
      </div>
    </td>
  </tr>
</template>

<script>
export default {
  name: "TableRow",
  props: ['datas','buttons'],
}
</script>