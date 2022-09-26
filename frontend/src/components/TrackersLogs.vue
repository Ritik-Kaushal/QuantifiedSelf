<template>
    <div>This is trackers logs details page</div>
  </template>
  
  <script>
  export default {
    name: "TrackersLogsDetails",
    mounted(){
        this.update_active()
    },
    methods : {
        update_active(){
            this.$store.commit("change_active",2);
        }
    }
  };
  </script>