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
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th scope="col">S.N.</th>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Latest Value</th>
            <th scope="col">Last Edited</th>
            <!-- <th scope="col">View</th> -->
          </tr>
        </thead>
        <tbody
          v-for="(eachTracker, index) in trackers"
          :key="eachTracker['id']"
        >
          <tr>
            <th scope="row">{{ index+1 }}</th>
            <td>{{ eachTracker["name"] }}</td>
            <td>{{ eachTracker["type"] }}</td>
            <td>{{ eachTracker["latest_value"] }}</td>
            <td>{{ eachTracker["last_edited"] }}</td>
            <!-- <td>
              <a
                class="btn btn-primary"
                href="/trackers?tracker_id={{ eachTracker[4] }}&duration_id=1"
                role="button"
                >View Tracker Details</a
              >
            </td> -->
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
};
</script>
