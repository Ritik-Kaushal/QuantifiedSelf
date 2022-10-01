<template>
  <div>
    <!-- Trigger for Delete Modal -->
    <div class="mt-2">
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#deleteTrackerModal"
      >
        Delete this Tracker
      </button>
    </div>
    <!-- Trigger for Delete Modal -->

    <!-- Delete Modal -->
    <div
      class="modal fade"
      id="deleteTrackerModal"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header justify-content-center">
            <h5 class="modal-title" id="staticBackdropLabel">
              Do you want to Delete this tracker
            </h5>
          </div>
          <div class="modal-body">
            <div class="alert alert-danger" role="alert" v-if="error">
              {{ error_msg }}
            </div>
            <form>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  name="check_point"
                  id="check_point"
                  v-model="what_to_do"
                />
                <label class="form-check-label" for="check_point"
                  >Do you really want to delete this tracker ?</label
                >
              </div>
              <div class="modal-footer">
                <button class="btn btn-primary" @click="deleteTracker($event)">
                  Yes
                </button>
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-bs-dismiss="modal"
                >
                  No
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- Delete Modal -->
  </div>
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "DeleteTrackerModal",
  data() {
    return {
      error: false,
      error_msg: "",
      what_to_do: false,
    };
  },
  methods: {
    async deleteTracker(e) {
      e.preventDefault();
      if (this.what_to_do) {
        let url =
          "http://localhost:5000/api/trackers/delete?tracker_id=" +
          this.$store.getters.get_selected_tracker_id;
        let init_obj = {
          method: "DELETE",
          mode: "cors",
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
            this.$store.commit("set_ready_to_display_tracker_cards", false);
            $("#deleteTrackerModal").modal("hide");

            await this.$store.dispatch("getTrackers");
            this.$store.commit(
              "change_selected_tracker_id",
              this.$store.getters.get_tracker_list[0].id
            );
            await this.$store.dispatch("getSelectedTrackerDetails");
            await this.$store.dispatch('getDataSummary');
            this.$store.commit("set_ready_to_display_tracker_cards", true);
          })
          .catch((e) => {
            this.error_msg = e.message;
            this.error = true;

            const err = JSON.parse(e.message);

            if (err.error_code == "TIM" || err.error_code == "IVT") {
              this.$store.dispatch('logoutUser');

            }
          });
      } else {
        this.error_msg = "Please check the checkbox to delete";
        this.error = true;
      }
    },
  },
};
</script>
