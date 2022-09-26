<template>
  <div>This is trackers details page</div>
</template>

<script>
export default {
  name: "TrackersDetails",
  mounted(){
        this.update_active()
    },
    methods : {
        update_active(){
            this.$store.commit("change_active",1);
        }
    }
};
</script>
