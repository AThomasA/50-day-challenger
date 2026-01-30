import { useEffect, useState } from "react";
import { api } from "../services/api";

export function useFinance() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(false);

  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  useEffect(() => {
    let isMounted = true; // evita setState se desmontar

    async function loadDashboard() {
      setLoading(true);

      try {
        const params = {};

        if (startDate) params.start_date = startDate;
        if (endDate) params.end_date = endDate;

        const response = await api.get("/dashboard/", { params });

        if (isMounted) {
          setSummary(response.data);
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    loadDashboard();

    return () => {
      isMounted = false;
    };
  }, [startDate, endDate]);

  return {
    summary,
    loading,

    startDate,
    endDate,

    setStartDate,
    setEndDate,
  };
}
