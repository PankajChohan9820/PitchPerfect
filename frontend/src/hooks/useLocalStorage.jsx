import { useState } from "react";

export const useLocalStorage = () => {
  const [value, setValue] = useState<string | null>(null);

  const setItem = (key, value) => {
    localStorage.setItem(key, value);
    setValue(value);
  };

  const getItem = (key) => {
    const storedValue = localStorage.getItem(key);
    if (storedValue !== null) {
      setValue(storedValue);
    }
    return storedValue;
  };

  const removeItem = (key) => {
    localStorage.removeItem(key);
    setValue(null);
  };

  return { value, setItem, getItem, removeItem };
};
