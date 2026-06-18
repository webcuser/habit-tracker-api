<template>
  <div id="app">
    <h1>Habit Tracker</h1>
    <ul>
      <li v-for="habit in habits" :key="habit.id">
        {{ habit.name }} - Completed: {{ habit.completed }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      habits: []
    };
  },
  mounted() {
    this.fetchHabits();
  },
  methods: {
    async fetchHabits() {
      const response = await axios.get('http://localhost:8000/habits/');
      this.habits = response.data;
    }
  }
};
</script>
