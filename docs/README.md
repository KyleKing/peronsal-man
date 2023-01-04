# personal-man (`pman`)

> **Note**
>
> I am archiving this project in favor of [cheat](https://github.com/cheat/cheat), which provides the same features and more!

Personal Manpages

## Installation

1. [Install `ripgrep`](https://github.com/BurntSushi/ripgrep/tree/000015791742bb1280f1853adb714fdee1ba9f8e#installation)

1. Install the `pman` CLI with pipx

   ```sh
   pipx install personal-man
   ```

1. Run `pman` to check that installation succeeded and to see the available commands

1. The help output will display the directory for your personal manpages, but you can change the default by exporting an environment variable: `PMAN_DOC_PATH`. I personally have a directory within my main Obsidian vault so that I can edit the files in [Obsidian](https://obsidian.md/) and search with `pman`

## Usage

![VHS Demo](./demo.gif)

For more example code, see the [scripts] directory or the [tests].

## Project Status

See the `Open Issues` and/or the [CODE_TAG_SUMMARY]. For release history, see the [CHANGELOG].

## Contributing

We welcome pull requests! For your pull request to be accepted smoothly, we suggest that you first open a GitHub issue to discuss your idea. For resources on getting started with the code base, see the below documentation:

- [DEVELOPER_GUIDE]
- [STYLE_GUIDE]

## Code of Conduct

We follow the [Contributor Covenant Code of Conduct][contributor-covenant].

### Open Source Status

We try to reasonably meet most aspects of the "OpenSSF scorecard" from [Open Source Insights](https://deps.dev/pypi/personal_man)

## Responsible Disclosure

If you have any security issue to report, please contact the project maintainers privately. You can reach us at [dev.act.kyle@gmail.com](mailto:dev.act.kyle@gmail.com).

## License

[LICENSE]

[changelog]: ./docs/CHANGELOG.md
[code_tag_summary]: ./docs/CODE_TAG_SUMMARY.md
[contributor-covenant]: https://www.contributor-covenant.org
[developer_guide]: ./docs/DEVELOPER_GUIDE.md
[license]: https://github.com/kyleking/personal-man/LICENSE
[scripts]: https://github.com/kyleking/personal-man/scripts
[style_guide]: ./docs/STYLE_GUIDE.md
[tests]: https://github.com/kyleking/personal-man/tests
