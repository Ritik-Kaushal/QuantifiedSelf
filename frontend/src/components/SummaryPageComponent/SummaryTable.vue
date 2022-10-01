<template>
  <!-- Table for all trackers -->
  <div class="container-fluid">
    <!-- Divider -->
    <hr class="dropdown-divider" />
    <!-- Divider -->

    <div class="row mt-2">
      <div class="col-md-12 fw-bold fs-5 text-center mt-5">
        List of Trackers
      </div>
    </div>

    <!-- Divider -->
    <hr class="dropdown-divider" />
    <!-- Divider -->

    <div class="row mt-2">
      <table class="table table-stripped table-hover">
        <thead>
          <tr>
            <th scope="col">S.N.</th>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Latest Value</th>
            <th scope="col">Last Edited</th>
            <th scope="col">View</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(eachTracker, index) in trackers"
          :key="eachTracker['id']">
            <th scope="row">{{ index+1 }}</th>
            <td>{{ eachTracker["name"] }}</td>
            <td>{{ eachTracker["type"] }}</td>
            <td>{{ eachTracker["latest_value"] }}</td>
            <td>{{ eachTracker["last_edited"] }}</td>
            <td>
              <button class="btn btn-primary" role="button" @click="view_tracker($event,eachTracker['id'])">
                View Tracker Details
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "SummaryTable",
  props: ["trackers"], // It is a list which contains trackers as objects. Each object has id, name, type,lastest_value,last_edited
  methods : {
    view_tracker(e,tracker_id){
      this.$store.commit('change_selected_tracker_id',tracker_id);
      this.$store.dispatch('getSelectedTrackerDetails');
      this.$router.push({path : '/dashboard/trackers'});
    }
  }
};
</script>
