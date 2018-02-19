<template>
  <div class="field is-grouped">
    <p v-if="save" class="control">
      <a class="button is-success">
        <span class="icon is-small">
          <i class="fas fa-check"></i>
        </span>
        <span>Save</span>
      </a>
    </p>
    <p v-if="reload" class="control">
      <a class="button is-info">
        <span class="icon is-small">
          <i class="fas fa-sync"></i>
        </span>
      </a>
    </p>
  </div>
</template>

<script>
export default {
  name: "button-goup",
  props: ['save', 'reload']
}
</script>

<style>

</style>
