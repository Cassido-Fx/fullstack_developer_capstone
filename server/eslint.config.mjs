import typescriptParser from "@typescript-eslint/parser"; // Import the parser
import typescriptEslint from "@typescript-eslint/eslint-plugin";
import eslintPluginReact from "eslint-plugin-react";

export default [
  {
    languageOptions: {
      parser: typescriptParser, // Assign the parser
    },
    plugins: {
      "@typescript-eslint": typescriptEslint,
      react: eslintPluginReact,
    },
    rules: {
      // Your rules here
    },
  },
];
