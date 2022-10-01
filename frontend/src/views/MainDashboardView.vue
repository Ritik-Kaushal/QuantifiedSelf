<template>
  <div >
      <DashboardNavbar />
      <router-view class="router-view-div" />
    
  </div>
</template>

<script>
import validateToken from "@/utils/validateToken";
import DashboardNavbar from "@/components/Dashboard-navbar.vue";

export default {
  name: "DashboardView",
  components: {
    DashboardNavbar,
  },
  mounted(){
    if(this.$store.getters.get_login_status && validateToken()){
      this.$store.dispatch("getTrackers");
    }
    else{
      this.$store.dispatch("logoutUser");
    }
  }
};
</script>

<style scoped>
.router-view-div{
  position: relative;
  top:56px;
  margin:5px 5px 5px 5px;
}

@media (min-width: 800px) {
  .router-view-div{
    margin-left:275px;
  }
}
</style>