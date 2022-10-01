<template>
  <div v-if="$store.getters.get_ready_to_display_logs">
    <div v-if="$store.getters.get_are_trackers_available">
      <DropDown />
    <TrackerLogs_Details />
    </div>
    <div v-else>
      <NoLogs/>
    </div>
  </div>
</template>

<script>
import DropDown from "../components/dropdown.vue";
import TrackerLogs_Details from "../components/trackerLogs_details.vue";
import NoLogs from "../components/no_logs_page.vue";
export default {
  name: "TrackersLogsDetails",
  components: {
    DropDown,
    TrackerLogs_Details,
    NoLogs
  },
  async mounted() {
    console.log(1000);
    this.$store.commit("set_ready_to_display_logs",false);
    this.$store.commit("change_active", 2);
    if (this.$store.getters.need_to_reload_logs) {
      console.log("1001");
      await this.$store.dispatch("getLogs");
    }
    this.$store.commit("set_ready_to_display_logs",true);
  }
};
</script>
