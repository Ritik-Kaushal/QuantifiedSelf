<template>
  <div>
    <!-- Trigger for Update Details Modal -->
    <div class="mt-2">
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#updateTrackerModal"
      >
        Update Details
      </button>
    </div>
    <!-- Trigger for Update Details Modal -->

    <!-- Update Details Modal -->
    <div
      class="modal fade"
      id="updateTrackerModal"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header justify-content-center">
            <h5 class="modal-title" id="staticBackdropLabel">Update Details</h5>
          </div>
          <div class="modal-body">
            <div class="alert alert-danger" role="alert" v-if="error">
              {{ error_msg }}
            </div>

            <form>
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
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Tracker Type</span
                >
                <input
                  class="form-control"
                  type="text"
                  name="tracker_type"
                  :value="tracker_type"
                  aria-label="Disabled input example"
                  disabled
                  readonly
                />
              </div>
              <div v-if="tracker_type == 'Multiple Choice'">
                <div class="input-group mb-3">
                  <span class="input-group-text" id="inputGroup-sizing-default"
                    >Tracker Values</span
                  >
                  <input
                    type="text"
                    class="form-control"
                    aria-label="Sizing example input"
                    aria-describedby="inputGroup-sizing-default"
                    name="tracker_values"
                    v-model="values"
                  />
                </div>
              </div>
              <div class="modal-footer">
                <button class="btn btn-primary" @click="updateTracker($event)">
                  Update
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
    <!-- Update Details Modal -->
  </div>
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "UpdateTrackerModal",
  data() {
    return {
      error: false,
      error_msg: "",
      tracker_name: this.$store.getters.get_selected_tracker.tracker_name,
      tracker_description:
        this.$store.getters.get_selected_tracker.tracker_description,
      tracker_type: this.$store.getters.get_selected_tracker.tracker_type,
      values: this.$store.getters.get_selected_tracker.reqd_values,
    };
  },
  methods: {
    async updateTracker(e) {
      e.preventDefault();
      let data = {
        tracker_id: this.$store.getters.get_selected_tracker.id,
        tracker_name: this.tracker_name,
        tracker_description: this.tracker_description,
        tracker_values: this.tracker_values,
      };
      let url = "http://localhost:5000/api/trackers/put";
      let init_obj = {
        method: "PUT",
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
          console.log(11);
          $("#updateTrackerModal").modal("hide");
          await this.$store.dispatch("getTrackers");
          this.$store.commit("change_selected_tracker_id", d.id);
          await this.$store.dispatch("getSelectedTrackerDetails");
          
        })
        .catch((e) => {
          this.error_msg = e.message;
          this.error = true;

          const err = JSON.parse(e.message);

            if (err.error_code == "TIM" || err.error_code == "IVT") {
              this.$store.dispatch('logoutUser');
            }
        });
    },
  },
};
</script>
