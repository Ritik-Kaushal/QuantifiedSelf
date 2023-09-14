<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",

  created() {
    document.title = 'Quantified Self'; // Set the page title
  },
};
</script>

