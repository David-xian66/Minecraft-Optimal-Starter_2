import functools
import os
import subprocess
import sys

import click


# TODO: CAMPid 0970432108721340872130742130870874321
def import_it(*segments):
    import importlib
    import pkg_resources

    major = int(pkg_resources.get_distribution(__name__.partition('.')[0]).version.partition(".")[0])

    m = {
        "pyqt_tools": "pyqt{major}_tools".format(major=major),
        "pyqt_plugins": "pyqt{major}_plugins".format(major=major),
        "qt_tools": "qt{major}_tools".format(major=major),
        "qt_applications": "qt{major}_applications".format(major=major),
    }

    majored = [m[segments[0]], *segments[1:]]
    return importlib.import_module(".".join(majored))

qt_applications = import_it("qt_applications")
qt_tools = import_it("qt_tools")


fspath = getattr(os, 'fspath', str)


@click.group()
def main():
    pass


def run(
        application_name,
        args=(),
        environment=os.environ,
        sys_platform=sys.platform,
):
    modified_environment = qt_tools.create_environment(
        reference=environment,
    )

    command_elements = qt_tools.create_command_elements(
        name=application_name,
        sys_platform=sys_platform,
    )

    completed_process = subprocess.run(
        [*command_elements, *args],
        env=modified_environment,
    )

    return completed_process.returncode


# written by build.py

# @main.command(
#     add_help_option=False,
#     context_settings={
#         'ignore_unknown_options': True,
#         'allow_extra_args': True,
#     },
# )
# @click.pass_context
# def designer(ctx):
#     return run('designer', args=ctx.args)

# ----  start of generated wrapper entry points


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def androiddeployqt(ctx):
    return run('androiddeployqt', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def androidtestrunner(ctx):
    return run('androidtestrunner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def assistant(ctx):
    return run('assistant', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def designer(ctx):
    return run('designer', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lconvert(ctx):
    return run('lconvert', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def licheck64(ctx):
    return run('licheck64', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def linguist(ctx):
    return run('linguist', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lrelease(ctx):
    return run('lrelease', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def lupdate(ctx):
    return run('lupdate', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def pixeltool(ctx):
    return run('pixeltool', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdbus(ctx):
    return run('qdbus', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdbuscpp2xml(ctx):
    return run('qdbuscpp2xml', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdbusviewer(ctx):
    return run('qdbusviewer', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdbusxml2cpp(ctx):
    return run('qdbusxml2cpp', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdistancefieldgenerator(ctx):
    return run('qdistancefieldgenerator', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qdoc(ctx):
    return run('qdoc', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qhelpgenerator(ctx):
    return run('qhelpgenerator', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmake(ctx):
    return run('qmake', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmake6(ctx):
    return run('qmake6', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qml(ctx):
    return run('qml', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlcachegen(ctx):
    return run('qmlcachegen', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmleasing(ctx):
    return run('qmleasing', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlformat(ctx):
    return run('qmlformat', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlimportscanner(ctx):
    return run('qmlimportscanner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmllint(ctx):
    return run('qmllint', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlplugindump(ctx):
    return run('qmlplugindump', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlpreview(ctx):
    return run('qmlpreview', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlprofiler(ctx):
    return run('qmlprofiler', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmlscene(ctx):
    return run('qmlscene', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmltestrunner(ctx):
    return run('qmltestrunner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmltime(ctx):
    return run('qmltime', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qmltyperegistrar(ctx):
    return run('qmltyperegistrar', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qt_cmake(ctx):
    return run('qt-cmake', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qt_cmake_private(ctx):
    return run('qt-cmake-private', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qt_cmake_standalone_test(ctx):
    return run('qt-cmake-standalone-test', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qt_configure_module(ctx):
    return run('qt-configure-module', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtattributionsscanner(ctx):
    return run('qtattributionsscanner', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtdiag(ctx):
    return run('qtdiag', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtdiag6(ctx):
    return run('qtdiag6', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtpaths(ctx):
    return run('qtpaths', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtplugininfo(ctx):
    return run('qtplugininfo', args=ctx.args)


@main.command(
    add_help_option=False,
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
def qtwaylandscanner(ctx):
    return run('qtwaylandscanner', args=ctx.args)


# ----  end of generated wrapper subcommands

