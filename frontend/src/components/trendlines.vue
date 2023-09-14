<template>
  <div>
    <div class="container-fluid">
      <div class="row mt-2">
        <div class="col-md-12 fw-bold fs-5 text-center mt-5">Trendlines</div>
      </div>
      <!-- Divider -->
      <hr class="dropdown-divider" />
      <!-- Divider -->

      <div class="row mt-4" id="trendlines"></div>
    </div>
    <!-- Trend Line -->
  </div>
</template>

<script>
export default {
  name: "TrendLines",
  async mounted() {
    await this.generate_trendlines();
  },
  methods: {
    async generate_trendlines() {
      for (let each of this.$store.getters.get_tracker_list) {
        console.log("Tracker =======================", each);
        await this.$store.dispatch("get_chart_data", {
          tracker_values: each.reqd_values,
          tracker_type: each.type,
          tracker_id: each.id,
          duration_id: 1,
          title: each.name,
        });
        if (this.$store.getters.get_chart_data.labels.length == 0) {
          console.log(each.id, "Here");
          this.addNoTrendlineImage(each.name);
        } else {
          this.addCanvas(each.id);
          await this.$store.dispatch("generate_chart", each.id);
        }
      }
    },
    addNoTrendlineImage(tracker_name) {
      let templateString =
        '<div class="col-md-6 mb-3" <div class="card text-dark bg-light mb-3 h-100 text-center" style="max-width: 100rem;"> <div class="card-body"> No Data is Available for ' +
        tracker_name +
        "</div> </div> </div>";
      $("#trendlines").append(templateString);
    },
    addCanvas(tracker_id) {
      const id = "chart_id_" + tracker_id.toString();
      let templateString =
        '<div class="col-md-6 mb-3" <div class="card text-dark bg-light mb-3 h-100 text-center" style="max-width: 100rem;"> <div class="card-body">  <div> <canvas id="' +
        id +
        '"></canvas> </div> </div> </div> </div>';
      $("#trendlines").append(templateString);
    },
  },
};
</script>
