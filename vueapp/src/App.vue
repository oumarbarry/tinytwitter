<script setup>
import { onMounted } from 'vue'

let message = $ref('')
let name = $ref('')
let tweets = $ref([])

const postTweet = async () => {
  const response = await fetch('http://localhost:8000/api/tweets/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, name }),
  })
  const data = await response.json()
  tweets.push(data)

  message = ''
  name = ''
}

const getTweets = async () => {
  const response = await fetch('http://localhost:8000/api/tweets/')
  tweets = await response.json()
}

onMounted(async () => {
  await getTweets()
})
</script>

<template>
  <main class="m-5">
    <form @submit.prevent="postTweet">
      <div class="row">
        <div class="col">
          <input v-model="message" type="text" class="form-control" placeholder="Message" maxlength="50" aria-label="Message" required>
        </div>
        <div class="col">
          <input v-model="name" type="text" class="form-control" placeholder="Name" aria-label="Name" required>
        </div>
        <div class="col-auto">
          <button type="submit" class="btn btn-primary">Tweet</button>
        </div>
      </div>
    </form>

    <table class="table mt-5">
      <thead>
        <tr>
          <th scope="col">Created At</th>
          <th scope="col">Message</th>
          <th scope="col">Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="tweet in tweets" :key="tweet.id">
          <td>{{ new Date(tweet.created_at).toUTCString() }}</td>
          <td>{{ tweet.message }}</td>
          <td>{{ tweet.name }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>
