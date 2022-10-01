<template>
  <div>
    <!-- Trigger for Create Tracker Modal -->
    <div class="mt-2">
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#createTrackerModal"
      >
        + Add a Tracker
      </button>
    </div>
    <!-- Trigger for Create Tracker Modal -->

    <!-- Create Tracker Modal -->
    <div
      class="modal fade"
      id="createTrackerModal"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header justify-content-center">
            <h5 class="modal-title" id="staticBackdropLabel">Create Tracker</h5>
          </div>
          <div class="modal-body">
            <div class="alert alert-danger" role="alert" v-if="error">
              {{ error_msg }}
            </div>
            <form>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Tracker Type</span
                >
                <select
                  class="form-select form-control mb-3"
                  aria-label="Sizing example input"
                  name="tracker_type"
                  v-model="tracker_type"
                >
                  <option
                    v-for="each in $store.getters.get_tracker_type_list"
                    :key="each.id"
                  >
                    {{ each.type }}
                  </option>
                </select>
              </div>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Tracker Name</span
                >
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="tracker_name"
                  v-model="tracker_name"
                />
              </div>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Tracker Description</span
                >
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="tracker_description"
                  v-model="tracker_description"
                />
              </div>

              <div
                class="input-group mb-3"
                v-if="tracker_type == 'Multiple Choice'"
              >
                <span
                  class="input-group-text d-grid gap-2 mb-1"
                  id="inputGroup-sizing-default"
                  >Tracker Values(only for multiple choice, separate by
                  comma)</span
                >
                <input
                  class="form-control"
                  type="text"
                  name="tracker_values"
                  v-model="tracker_values"
                />
              </div>
              <div class="modal-footer">
                <button
                  class="btn btn-primary"
                  @click="createTrackerForm($event)"
                >
                  Create
                </button>
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-bs-dismiss="modal"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- Create Tracker Modal -->
  </div>
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "CreateTrackerModal",
  data() {
    return {
      error: false,
      error_msg: "",
      tracker_name: "",
      tracker_description: "",
      tracker_type: "",
      tracker_values: "",
    };
  },
  methods: {
    async createTrackerForm(e) {
      e.preventDefault();
      console.log(
        this.tracker_description,
        this.tracker_name,
        this.tracker_type,
        this.tracker_values
      );
      let data = {
        tracker_name: this.tracker_name,
        tracker_type: this.tracker_type,
        tracker_description: this.tracker_description,
        tracker_values: this.tracker_values,
      };
      let url = "http://localhost:5000/api/trackers/post";
      let init_obj = {
        method: "POST",
        mode: "cors",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      };

      let res = await FetchFunction({
        url: url,
        init_obj: init_obj,
        authRequired: true,
      })
        .then(async (d) => {
          $('#createTrackerModal').modal('hide');
          
          await this.$store.dispatch("getTrackers");
          await this.$store.dispatch('getDataSummary');
          this.$store.commit("change_selected_tracker_id", d.id);
          await this.$store.dispatch("getSelectedTrackerDetails");
        })
        .catch((e) => {
          const err = JSON.parse(e.message);
          
          this.error_msg = err.error_message;
          this.error = true;

          if(err.error_code == 'TIM' || err.error_code == 'IVT'){
            this.$store.dispatch('logoutUser');

          }
        }).catch();
    },
  },
};
</script>
