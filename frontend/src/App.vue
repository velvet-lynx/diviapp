<template>
  <!--<nav class="navbar">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        <h1>DiviApp</h1>
      </a>
      <button class="button navbar-burger">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>-->

  <admin></admin>
</template>

<script>
import admin from "./components/Admin.vue";

export default {
  name: 'app',
  data () {
    return {
    }
  },
  components: {
    admin
  }
}
</script>

<style>

</style>
