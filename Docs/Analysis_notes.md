Observation: Merge Commit vs Squash Merge
In a merge commit, all commits from the feature branch are preserved in the history. The branch structure is visible, and Git creates an additional merge commit to combine changes.
In a squash merge, all commits from the feature branch are combined into a single commit before merging. This results in a cleaner and more linear history.
Merge commits are useful when we want to retain detailed development history, while squash merge is preferred when we want a simplified and clean commit history.