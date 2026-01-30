import { useEffect, useState, useCallback } from "react";
import { api, createRevenue } from "../services/api";

export function useFinance() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(false);

  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  // Função central de carga do dashboard
  const fetchDashboard = useCallback(async () => {
    setLoading(true);

    try {
      const params = {};

      if (startDate) params.start_date = startDate;
      if (endDate) params.end_date = endDate;

      const response = await api.get("/dashboard/", { params });
      setSummary(response.data);
    } catch (error) {
      console.error("Erro ao carregar dashboard", error);
    } finally {
      setLoading(false);
    }
  }, [startDate, endDate]);

  // Dispara automaticamente ao mudar período
  useEffect(() => {
    fetchDashboard();
  }, [fetchDashboard]);

  // POST Receita
  const addRevenue = async (data) => {
    try {
      await createRevenue(data);
      await fetchDashboard(); // Recarrega o dashboard após adicionar receita
    } catch (error) {
      console.error("Erro ao criar receita", error);
      throw error;
    }
  };

  return {
    summary,
    loading,

    addRevenue,

    startDate,
    endDate,
    setStartDate,
    setEndDate,
  };
}
