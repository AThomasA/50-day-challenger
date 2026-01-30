import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:8000/finance/api",
});

// Receita
export const createRevenue = (data) => api.post("/revenues/", data);

// Dashboard
export const getDashboard = (params) =>
  api.get("/dashboard/", { params });