<template>
    <div class="container mt-2">
        <h1 class="mb-3">Ask a Question</h1>
        <form @submit.prevent="onSubmit">
            <textarea 
                v-model="questionBody"
                class="form-control" 
                placeholder="What do you want to ask?"
                rows="3"
            ></textarea>
            <button type="submit" class="btn btn-success mt-3">Publish</button>
        </form>
        <p v-if="error" class="error mt-2">{{ error }}</p>
    </div>
</template>

<script>
import { axios } from "@/common/api.service.js";
export default {
    name: "QuestionEditor",
    data() {
        return {
            questionBody: null,
            error: null
        }
    },
    methods: {
        onSubmit() {
            // perform basic validation and eventually call this.performNetworkRequest;
            if (!this.questionBody) {
                this.error = "You can't send an empty question!";
            } else if (this.questionBody.length > 240) {
                this.error = "Ensure this field has no more than 240 characters!";
            } else {
                this.performNetworkRequest(); 
                // call the function that will make the network request, this is the function that will make the POST request to the API
            }
        },
        async performNetworkRequest() {
            // Tell the REST API to create or update a Question instance;
            let endpoint = "/api/v1/questions/";
            let method = "POST";
            if (this.slug !== undefined && this.slug !== "") {
                endpoint += `${this.slug}/`;
                method = "PUT";
            }
            try {
                const response = await axios({
                    method: method,
                    url: endpoint,
                    data: { content: this.questionBody },
                });
                this.$router.push({
                    name: "question",
                    params: { slug: response.data.slug },
                });
            } catch (error) {
                this.error = error.response.statusText;
            }
        },
        

    }
}
</script>