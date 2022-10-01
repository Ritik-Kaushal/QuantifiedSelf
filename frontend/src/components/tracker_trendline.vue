<template>
  <div>
    <div class="container-fluid">
      <div class="row mt-2">
        <div class="col-md-12 fw-bold fs-5 text-center mt-5">Trendlines</div>
      </div>
      <!-- Divider -->
      <hr class="dropdown-divider" />
      <!-- Divider -->

      <div class="row mt-4" id="tracker_trendlines"></div>
    </div>
    <!-- Trend Line -->
  </div>
</template>

<script>

export default {
  name: "TrackerTrendline",
  async mounted() {
    if (this.$store.getters.get_selected_tracker.id == undefined) {
        console.log("Here in");
        await this.$store.dispatch('getTrackers');
    }
    await this.generate_trendlines();
  },
  methods: {
    async generate_trendlines(){
        let obj = {
        tracker_values: this.$store.getters.get_selected_tracker.reqd_values,
        tracker_type: this.$store.getters.get_selected_tracker.tracker_type,
        tracker_id: this.$store.getters.get_selected_tracker.id,
        duration_id: this.$store.getters.get_selected_duration_id,
        title: this.$store.getters.get_selected_tracker.tracker_name,
      };
      console.log(123456789,obj)
      console.log(
          typeof(this.$store.getters.get_selected_tracker.id),
        );
    await this.$store.dispatch("get_chart_data", obj);
      if (this.$store.getters.get_chart_data.labels.length == 0) {
        console.log(
          this.$store.getters.get_selected_tracker.id,
          "Here"
        );
        this.addNoTrendlineImage(
          this.$store.getters.get_selected_tracker.tracker_name
        );
      } else {
        
        this.addCanvas(this.$store.getters.get_selected_tracker.id);
        await this.$store.dispatch(
          "generate_chart",
          this.$store.getters.get_selected_tracker.id
        );
      }
    },
    addNoTrendlineImage(tracker_name) {
      let templateString =
        '<div class="col-md-6 mb-3" <div class="card text-dark bg-light mb-3 h-100 text-center" style="max-width: 100rem;"> <div class="card-body"> No Data is Available for' +
        tracker_name +
        "</div> </div> </div>";
      $("#tracker_trendlines").append(templateString);
    },
    addCanvas(tracker_id) {
        const id = "chart_id_"+tracker_id.toString();
      let templateString =
        '<div class="col-md-6 mb-3" <div class="card text-dark bg-light mb-3 h-100 text-center" style="max-width: 100rem;"> <div class="card-body">  <div> <canvas id="' +
        id +
        '"></canvas> </div> </div> </div> </div>';
      $("#tracker_trendlines").append(templateString);
    },
  },
};
</script>
