<template>
  <div>
    <TopNavBar :key="this.$store.state.user_store.loggedIn" />
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
