<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12 fw-bold fs-5 text-center">
        Tracker Details and Stats
      </div>
    </div>

    <hr class="dropdown-divider" />

    <div class="row mt-4">
      <!-- For Tracker Details -->
      <div class="col-md-4 mb-3">
        <div
          class="card text-dark bg-info mb-3 h-100"
          style="max-width: 100rem"
        >
          <div class="card-header text-center">
            <span class="fw-bold">
              <h3>Tracker Details</h3>
            </span>
          </div>
          <div class="card-body">
            <h5 class="card-title">
              <span class="fw-bold">Name :&nbsp;</span>
              {{ $store.getters.get_selected_tracker.tracker_name }}
            </h5>
            <h5 class="card-title">
              <span class="fw-bold">Description :&nbsp;</span>
              {{ $store.getters.get_selected_tracker.tracker_description }}
            </h5>
            <h5 class="card-title">
              <span class="fw-bold">Type :&nbsp;</span>
              {{ $store.getters.get_selected_tracker.tracker_type }}
            </h5>

            <h5
              class="card-title"
              v-if="
                $store.getters.get_selected_tracker.tracker_type ==
                'Multiple Choice'
              "
            >
              <span class="fw-bold">Values :&nbsp;</span>
              {{ $store.getters.get_selected_tracker.reqd_values }}
            </h5>
          </div>
        </div>
      </div>
      <!-- For Tracker Details -->
      <!-- For Stats -->
      <div class="col-md-4 mb-3">
        <div
          class="card text-dark bg-info mb-3 h-100"
          style="max-width: 100rem"
        >
          <div class="card-header text-center">
            <span class="fw-bold">
              <h3>Stats</h3>
            </span>
          </div>
          <div class="card-body">
            <div v-if="$store.getters.get_selected_tracker.last_edited_date">
              <h5 class="card-title float-middle">
                <span class="fw-bold">Last Edited Date :&nbsp;</span>
                {{ $store.getters.get_selected_tracker.last_edited_date }}
              </h5>
              <h5 class="card-title float-middle">
                <span class="fw-bold">Last Edited Time :&nbsp;</span>
                {{ $store.getters.get_selected_tracker.last_edited_time }}
              </h5>
            </div>
            <div v-else>
              <h5 class="card-title float-middle">
                <span class="fw-bold">Last Edited Date :&nbsp;</span>
                -
              </h5>
              <h5 class="card-title float-middle">
                <span class="fw-bold">Last Edited Time :&nbsp;</span>
                -
              </h5>
            </div>
            <br />
          </div>
        </div>
      </div>
      <!-- For Stats -->
      <!-- Actions -->
      <div class="col-md-4 mb-3">
        <div
          class="card text-dark bg-info mb-3 h-100"
          style="max-width: 100rem"
        >
          <div class="card-header text-center">
            <span class="fw-bold">
              <h3>Actions</h3>
            </span>
          </div>
          <div class="card-body">
            <LogValueModal />
            <DeleteTrackerModal />
            <UpdateTrackerModal />
            <CreateTrackerModal />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import LogValueModal from "./modals/LogValueModal.vue";
  import DeleteTrackerModal from "./modals/DeleteTrackerModal.vue";
  import UpdateTrackerModal from "./modals/UpdateTrackerModal.vue";
  import CreateTrackerModal from "./modals/CreateTrackerModal.vue";
  export default {
    name: "Tracker_Details",
    components: {
      LogValueModal,
      DeleteTrackerModal,
      UpdateTrackerModal,
      CreateTrackerModal
  },
  };
  </script>