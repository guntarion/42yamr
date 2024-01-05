<template>
    <div>
        <p class="text-muted">Author {{ answer.author }} &#8901; {{ answer.created_at }}</p>
        <p style="white-space: pre-wrap;">{{ answer.yamrbody }}</p>
        <hr>
        <div v-if="isAnswerAuthor">
            <!-- <button class="btn btn-sm btn-warning me-1">Edit</button> -->
          <router-link
            :to="{ name: 'answer-editor', params: { uuid: answer.uuid } }"
            class="btn btn-sm btn-warning me-1"
            >Edit
          </router-link>
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
    computed: {
        isAnswerAuthor() {
            // console.log("isAnswerAuthor  " + this.answer.author + " - " + this.requestUser);
            // return true if the logged in user is also the author of the answer instance
            
            return this.answer.author === this.requestUser;
        },
    },
}
</script>