---
title: Adam Brown / gitlabfred · GitLab
source: https://gitlab.com/acourtneybrown/gitlabfred
author:
  - "[[Gitlabtemplate]]"
published: 2025-11-13
created: 2026-01-17
description: GitLab Assistant for Alfred
tags:
  - clippings
---
[release 0.5.1](https://gitlab.com/acourtneybrown/gitlabfred/-/commit/dc05fa7dcdc39eb1e637189cfb6ebee65c36f3f9)

[Adam Brown](https://gitlab.com/acourtneybrown) authored

[dc05fa7d](https://gitlab.com/acourtneybrown/gitlabfred/-/commit/dc05fa7dcdc39eb1e637189cfb6ebee65c36f3f9)

| Name | Last commit | Last update |
| --- | --- | --- |

[**README.md**](https://gitlab.com/acourtneybrown/gitlabfred/-/blob/main/README.md?ref_type=heads)

## Alfred GitLabFred

Helpful GitLab assistant for Alfred

## Usage

- Search repositories (public only without [GitLab Token](https://gitlab.com/acourtneybrown/#gitlab-token) set) via the keyword `glab`.
	- ⏎: Open the repo's GitLab page.
	- ⌘C: Copy the repo URL.
	- ⌃⏎: Clone the repo to a local folder and open in the Terminal.
	- ⌥⏎: Fork the repo & clone the fork to a local folder. Then open in Terminal.
- Access merge requests you have opened with keyword `glabmr`.
	- ⏎: Open the MR in the browser.
	- ⌘C: Copy the MR URL.
- Open recent GitLab issues you are involved in with `glabi`.
	- ⏎: Open the issue in the browser.
	- ⌘C: Copy the issue URL.
- Access your GitLab todos list with keyword `glabt`.
	- ⏎: Open the todo in the browser.
	- ⌃⏎: Mark the todo as done.
	- ⌘C: Copy the issue URL.

The `glab` prefix can be changed in the configuration page, thus affecting all the keywords.

## GitLab Token

1. Add the **GitLab Token** in the Alfred workflow configuration.
2. Or: export the token in your `.zshenv`.

```shell
# add this to your \`$HOME/.zshenv\`

# ($alfred_workflow_name is only populated by shell processes that called by Alfred)

if [[ "$alfred_workflow_name" == "GitLabFred" ]]; then

    # if using a password manager, you can do something like this 

    # (\`op\` being the CLI for 1Password)

    GITLAB_TOKEN=$(op plugin run -- glab config get token)

    export GITLAB_TOKEN

fi
```

## Installation

[➡️ Download the latest release](https://gitlab.com/acourtneybrown/gitlabfred/-/releases)