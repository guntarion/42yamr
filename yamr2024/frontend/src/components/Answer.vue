<template>
    <div>
        <p class="text-muted">Author {{ answer.author }} &#8901; {{ answer.created_at }}</p>
        <p style="white-space: pre-wrap;">{{ answer.yamrbody }}</p>
        <hr>
        <div v-if="isAnswerAuthor">
            <!-- <button class="btn btn-sm btn-warning me-1">Edit</button> -->
            <router-link :to="{ name: 'answer-editor', params: { uuid: answer.uuid } }"
                class="btn btn-sm btn-warning me-1">Edit
            </router-link>
            <button class="btn btn-sm btn-danger mx-1" @click="showDeleteConfirmationBtn = !showDeleteConfirmationBtn">
                Delete
            </button>
            <button v-show="showDeleteConfirmationBtn" class="btn btn-sm btn-outline-danger" @click="triggerDeleteAnswer">
                Yes, delete my answer!
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true,
        },
        requestUser: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            showDeleteConfirmationBtn: false,
        };
    },
    computed: {
        isAnswerAuthor() {
            console.log("isAnswerAuthor  " + this.answer.author + " - " + this.requestUser);
            // return true if the logged in user is also the author of the answer instance

            return this.answer.author === this.requestUser;
        },
    },
    methods: {
        triggerDeleteAnswer() {
            // emit an event to delete an answer instance
            this.$emit("delete-answer", this.answer);
        },
    },
}
</script>