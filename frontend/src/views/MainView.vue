<template>
  <div>
    <TopNavBar />
    <router-view />
  </div>
</template>

<script>
import TopNavBar from "@/components/navbar.vue";

export default {
  name: "MainView",
  components: {
    TopNavBar,
  },
};
</script>
