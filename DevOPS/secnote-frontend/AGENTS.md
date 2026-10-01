<!-- LOVABLE:BEGIN -->
> [!IMPORTANT]
> This project is connected to [Lovable](https://lovable.dev). Avoid rewriting
> published git history — force pushing, or rebasing/amending/squashing commits
> that are already pushed — as it rewrites history on Lovable's side and the
> user will likely lose their project history.
>
> Commits you push to the connected branch sync back to Lovable and show up in
> the editor, so keep the branch in a working state.
<!-- LOVABLE:END -->

- Keep the secnote interface in TanStack Start and call the existing FastAPI incident endpoints from the browser using a user-configured API origin, because the Python service is hosted separately from this frontend.
- Mirror the repository's password scoring locally without transmitting password text, because its existing password endpoint returns HTML rather than JSON and local evaluation is safer for sensitive input.
