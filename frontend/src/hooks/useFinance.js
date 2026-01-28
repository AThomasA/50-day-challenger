import { useEffect, useState } from "react";
import { api } from "../services/api";

export function useFinance() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/dashboard/")
      .then((res) => setSummary(res.data))
      .finally(() => setLoading(false));
  }, []);

  return {
    summary,
    loading,
  };
}
